app:
	./josephmisiti.com
	
deploy:
	fab deploy -R website

install:
	go get
	
build:
	go build
	
