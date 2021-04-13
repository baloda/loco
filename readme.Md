# APIs:
    GET:http://127.0.0.1:8000/transactionservice/transaction/types/<str:type>/

    GET:http://127.0.0.1:8000/transactionservice/transaction/sums/<int:id>/

    GET/POST:http://127.0.0.1:8000/transactionservice/transaction/<int:id>/

    GET/PUT:http://127.0.0.1:8000/transactionservice/transaction/<int:id>/

    GET:http://127.0.0.1:8000/transactionservice/transaction/

    admin dashboard: http://127.0.0.1:8000/admin/


#### Start:

install docker
install docker-compose


run docker-compose up --build


Small data fixture has been addded using start_server.sh


# Curl Request:
```
curl --location --request GET '127.0.0.1:8000/transactionservice/transaction/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"parent_id": 1
}'
```

