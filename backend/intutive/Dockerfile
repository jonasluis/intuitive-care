# Usar imagem do OpenJDK 17
FROM openjdk:17-jdk-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o JAR gerado pelo Maven/Gradle
COPY target/minha-api.jar app.jar

# Expõe a porta da API
EXPOSE 8080

# Comando para rodar a API
ENTRYPOINT ["java", "-jar", "app.jar"]
