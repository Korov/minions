plugins {
    id("org.springframework.boot")
}

dependencies {
    implementation(project(":common"))
    implementation("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    annotationProcessor("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    implementation("com.google.guava:guava:${rootProject.extra.get("guavaVersion")}")
    testAnnotationProcessor("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    testImplementation("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.postgresql:postgresql:${rootProject.extra.get("postgresVersion")}")
    implementation("org.flywaydb:flyway-core:${rootProject.extra.get("flywayVersion")}")
    implementation("io.springfox:springfox-boot-starter:${rootProject.extra.get("springfoxVersion")}")
    implementation("org.springframework.boot:spring-boot-starter-data-mongodb")
    implementation("org.mybatis.spring.boot:mybatis-spring-boot-starter:${rootProject.extra.get("mybatisVersion")}")
    implementation("org.springframework.kafka:spring-kafka:2.7.6")
    implementation("com.baomidou:mybatis-plus-boot-starter:${rootProject.extra.get("mybatisPlusVersion")}")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.scala-lang:scala3-library_3:${rootProject.extra.get("scalaVersion")}")
    testImplementation("org.springframework.boot:spring-boot-starter-actuator")
    testImplementation("org.springframework.boot:spring-boot-devtools")
    testImplementation("com.baomidou:mybatis-plus-generator:${rootProject.extra.get("generatorVersion")}")
    testImplementation("org.apache.velocity:velocity-engine-core:${rootProject.extra.get("velocityVersion")}")
}

tasks.register<Copy>("copyJarKafkaConsumer") {
    copy {
        from("build/libs/kafka-consumer-${rootProject.extra.get("minionsVersion")}.jar"){
            rename("kafka-consumer-${rootProject.extra.get("minionsVersion")}.jar", "kafka-consumer.jar")
        }
        into("$buildDir/../../project_files/libs")
    }
}

tasks.build {
    finalizedBy(tasks.getByName("copyJarKafkaConsumer"))
}

java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

idea {
    module {
        isDownloadJavadoc = true
        isDownloadSources = true
    }
}

spotbugs {
    showProgress.set(true)
    ignoreFailures.set(true)
    tasks.spotbugsMain {
        reports.create("html") {
            isEnabled = true
            destination = file("$buildDir/reports/spotbugs/main/spotbugs.html")
            setStylesheet("fancy-hist.xsl")
        }
    }

    tasks.spotbugsTest {
        reports.create("html") {
            isEnabled = true
            destination = file("$buildDir/reports/spotbugs/test/spotbugs.html")
            setStylesheet("fancy-hist.xsl")
        }
    }
}

tasks.test {
    useJUnitPlatform {
        includeEngines("junit-jupiter")
    }
    reports{
        junitXml.required.set(false)
        html.required.set(true)
    }
    finalizedBy(tasks.jacocoTestReport)  // report is always generated after tests run
}

tasks.jacocoTestReport {
    dependsOn(tasks.test)  // tests are required to run before generating the report
}
