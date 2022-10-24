init:
	docker build -t everybody8/first:v1.0 .
tag:
	docker tag everybody8/first:v1.0 gcr.io/zuri-backend-project/first:v1.0
push:
	docker push gcr.io/zuri-backend-project/first:v1.0
deploy:
	gcloud run deploy --image gcr.io/zuri-backend-project/first:v1.0