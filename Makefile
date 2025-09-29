up:
	docker compose -f docker-compose-local.yaml up -docker
down:
	docker compose -f docker-compose-local.yaml down && network prune --force