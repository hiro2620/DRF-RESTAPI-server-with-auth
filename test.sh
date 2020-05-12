# GET
# DON'T forget to escape "/" to "%3A"
curl -X GET -H "Content-Type: application/json" \
-H "Authorization: JWT <YOUR ACCESS TOKEN>" \
localhost:8000/api/v1/schedules/?is_done=true&date_from=2020-05-08&date_to=2020-05-08&time_from=21%3A40%3A01&time_to=21%3A40%3A02


# POST
curl -X GET -H "Content-Type: application/json" \
-H "Authorization: JWT <YOUR ACCESS TOKEN>" \
-d '{"content":"22","date":"2020-5-22","time":"21:40"}' \


# PATCH
curl -X PATCH -H "Content-Type: application/json" \
-H "Authorization: JWT <YOUR ACCESS TOKEN>" \
-d '{"is_done":"false"}' \
localhost:8000/api/v1/schedules/054ae1ce-0444-4487-bcf7-69651285da40/


# DELETE
curl -X DELETE -H "Content-Type: application/json"\
-H "Authorization: JWT <YOUR ACCESS TOKEN>" \
localhost:8000/api/v1/schedules/918d539c-a9ad-4160-ba5e-51ab1b5127f9/