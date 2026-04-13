#1: компіляція
FROM gcc:latest AS builder
WORKDIR /app
COPY . .
RUN make

# 2: запуск
FROM debian:stable-slim
WORKDIR /app
COPY --from=builder /app/app .
CMD ["./app"]
