NOW=$(shell date)
WORKER=4

start:
	@echo "${NOW} start swarming..."
	@docker-compose up --scale worker=${WORKER}

down: 
	@echo "${NOW} down..."
	@docker-compose down
