import re
from datetime import datetime

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status, views, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from django_filters import rest_framework as filters 

from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleFilter(filters.FilterSet):

	date_from = filters.DateFilter(field_name="date", lookup_expr="gte")
	date_to   = filters.DateFilter(field_name="date", lookup_expr="lte")
	time_from = filters.TimeFilter(field_name="time", lookup_expr="gte")
	time_to   = filters.TimeFilter(field_name="time", lookup_expr="lte")


	class Meta:
		model = Schedule
		fields = ['is_done']


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object or admin user to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):

        # Instance must have an attribute named `owner`.
        return request.user.is_superuser or obj.owner == request.user


# Create your views here.
class ScheduleListCreateAPIView(generics.ListCreateAPIView):
	
	serializer_class = ScheduleSerializer
	permission_classes = [IsAuthenticated]

	filter_backends = [filters.DjangoFilterBackend]
	filterset_class = ScheduleFilter


	def get_serializer_context(self):
		"""
		Extra context provided to the serializer class.
		"""

		# add user's UUID to request.data so that seriarizer can read
		if self.request:
			self.request.data['owner'] = self.request.user.pk
		
		return {
			'request': self.request,
			'format': self.format_kwarg,
			'view': self
		}


	def get_queryset(self):
		'''
		This view should return a list of the schedules
        for the currently authenticated user.
		'''
		user = self.request.user

		# admin can read all users' schedules
		if user.is_superuser:
			return Schedule.objects.all()

		return Schedule.objects.filter(owner=user)


class ScheduleRetrieveUpdateDestroyAPIView(views.APIView):
	"""Class for retrieve, put, patch, delete schedule API"""

	permission_classes = [IsOwnerOrAdmin] # defined above. An original permission class

	def get_object(self):
		obj = get_object_or_404(Schedule, pk=self.kwargs["pk"]) # pk is spedified in url
		# check whether user has permission to access object or not
		# according to IsOwnerOrAdmin
		self.check_object_permissions(self.request, obj)
		return obj


	def get(self, request, pk, *args, **kwargs):
		"""A handler method to retrieve schedule object"""
		# get a model object
		schedule = self.get_object()
		# create a serializer object
		serializer = ScheduleSerializer(instance=schedule)
		# return a response object
		return Response(serializer.data, status.HTTP_200_OK)


	def put(self, request, pk, *args, **kwargs):
		"""A handler method to put (total update) schedule object"""
		# get model object
		schedule = self.get_object()
		# create a serializer object
		serializer = ScheduleSerializer(instance=schedule, data=request.data)
		# validation
		serializer.is_valid(raise_exception=True)
		# update the model object
		serializer.save()
		# return a response object
		return Response(serializer.data, status.HTTP_200_OK)


	def patch(self, request, pk, *args, **kwargs):
		"""A handler method to patch (partial update) schedule object"""
		# get model object
		schedule = self.get_object()
		# create a serializer object
		serializer = ScheduleSerializer(instance=schedule, data=request.data, partial=True)
		# validation
		serializer.is_valid(raise_exception=True)
		# update the model object partially
		serializer.save()
		# return a response object
		return Response(serializer.data, status.HTTP_200_OK)


	def delete(self, request, pk, *args, **kwargs):
		"""A handler method to delete schedule object"""
		# get model object
		schedule = self.get_object()
		# delete model object
		schedule.delete()
		# return model object
		return Response(status=status.HTTP_204_NO_CONTENT)