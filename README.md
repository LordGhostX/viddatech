# Public Rest API for Viddatech Paystack Consumption

## General API Information

* The base endpoint is: /
* All endpoints return JSON objects

## HTTP Return Codes

* HTTP 4XX return codes are used for malformed requests; the issue is on the sender's side
* HTTP 5XX return codes are used for internal errors; the issue is on Viddatech's side. It is important to NOT treat this as a failure operation; the execution status is UNKNOWN and could have been a success

## General Information on Endpoints

* For GET, POST endpoints, parameters must be sent along the request body
* Parameters may be sent in any order
* All endpoints returns success flag

Sample Payload below:

```JSON
{
    "success": true,
    "message": ""
}
```

## API Error

* Any endpoint can return an ERROR

Sample Payload below:

```JSON
{
    "success": false,
    "message": ""
}
```

## General endpoints

### Say hello

GET `/`

Says hello to the Rest API to test connectivity.

**Response**

```JSON
{
    "success": true,
    "message": "Hello World!"
}
```

### Create Transaction

POST `/new-transaction/`

Create a new transaction

**Parameters**

| Name      | Type    | Mandatory |
| --------- | ------- | --------- |
| email     | STRING  | YES       |
| amount    | INTEGER | YES       |
| reference | STRING  | YES       |

**Response**

```JSON
{
    "success": true,
    "message": "",
    "reference": "",
    "payment_url": ""
}
```

### Get Transactions

GET `/transactions/`

Get all account transactions

**Parameters**

| Name             | Type   | Mandatory |
| ---------------- | ------ | --------- |

**Response**

```JSON
{
    "success": true,
    "total": 0,
    "total_volume": 0,
    "message": "",
    "transactions": []
}
```

### Verify Transaction

POST `/verify-transaction/`

Verify a particular transaction

**Parameters**

| Name       | Type   | Mandatory |
| ---------- | ------ | --------- |
| reference  | STRING | YES       |      

**Response**

```JSON
{
    "success": true,
    "message": "",
    "data": []
}
```

### Get Balance

GET `/get-balance/`

Get Account Balance

**Parameters**

| Name       | Type   | Mandatory |
| ---------- | ------ | --------- |   

**Response**

```JSON
{
    "success": true,
    "message": "",
    "balance": 0
}
```

### Get Supported Banks

GET `/get-banks/`

Get Paystack Supported Banks

**Parameters**

| Name       | Type   | Mandatory |
| ---------- | ------ | --------- |   

**Response**

```JSON
{
    "success": true,
    "message": "",
    "data": []
}
```
