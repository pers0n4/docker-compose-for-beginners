# Docker Compose로 개발 생산성 높이기

## 실행

```bash
docker-compose up

# 백그라운드로 실행
docker-compose up -d

# 특정 서비스만 실행
docker-compose up backend ...

# 빌드하고 실행
docker-compose up --build
```

## 컨테이너 삭제

```bash
docker-compose down

# 연결된 볼륨 삭제
docker-compose down --volumes

# 생성된 이미지 삭제
docker-compose down --rmi local
```

## Docker Swarm

```bash
docker swarm init
docker swarm join-token (worker|manager)
docker swarm leave [--force]
docker node ls

docker service create --name registry --publish published=5000,target=5000 --constraint node.role==manager registry:2
docker-compose --file docker-stack.yaml build
docker-compose --file docker-stack.yaml push

docker-machine create --driver virtualbox --virtualbox-memory 1024 --engine-insecure-registry 127.0.0.1:5000 worker2

docker stack deploy --compose-file docker-stack.yaml STACK
docker stack services STACK
docker stack ps STACK
docker stack rm STACK
```
