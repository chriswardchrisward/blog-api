
'''

curl -X POST -d "username=cward&password=Test1234" http://127.0.0.1:8000/api/auth/token/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImN3YXJkIiwidXNlcl9pZCI6MSwiZW1haWwiOiJjaHJpc3dhcmRjaHJpc3dhcmRAZ21haWwuY29tIiwiZXhwIjoxNDgxMjM1NTk3fQ.OwrxpEOI67bkVwXwhnL6_b-8fx3JwN0jm7ag_Q_XwnU

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImN3YXJkIiwidXNlcl9pZCI6MSwiZW1haWwiOiJjaHJpc3dhcmRjaHJpc3dhcmRAZ21haWwuY29tIiwiZXhwIjoxNDgxMjM1NTk3fQ.OwrxpEOI67bkVwXwhnL6_b-8fx3JwN0jm7ag_Q_XwnU" http://127.0.0.1:8000/api/comments/

curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImN3YXJkIiwidXNlcl9pZCI6MSwiZW1haWwiOiJjaHJpc3dhcmRjaHJpc3dhcmRAZ21haWwuY29tIiwiZXhwIjoxNDgxMjM3OTQyfQ.DbRSD7NeCMQdqRuUlvtyAbvTgAGjpP6TnJPHq0z9WaE" -H "Content-Type: application/json" -d '{"content":"This is a curl reply to the curl test"}' 'http://127.0.0.1:8000/api/comments/create/?slug=yeah-buddy2&type=post&parent_id=18'

curl http://127.0.0.1:8000/api/comments/

'''