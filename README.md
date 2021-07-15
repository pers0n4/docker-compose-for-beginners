# Docker Compose로 개발 생성성 높이기

## 실행

```bash
docker-compose up

# 백그라운드로 실행
docker-compose up -d

# 특정 서비스만 실행
docker-compose up backend ...

# 빌드 실행
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
