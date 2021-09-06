plugins {
    id("org.springframework.boot")
}

val lombokVersion: String by rootProject.extra
val postgresVersion: String by rootProject.extra
val fastjsonVersion: String by rootProject.extra
val flywayVersion: String by rootProject.extra
val scalaVersion: String by rootProject.extra
val mybatisVersion: String by rootProject.extra
val springfoxVersion: String by rootProject.extra
val minionsVersion: String by rootProject.extra
val generatorVersion: String by rootProject.extra
val velocityVersion: String by rootProject.extra
val guavaVersion: String by rootProject.extra

dependencies {
    implementation(project(":common"))
    implementation("org.projectlombok:lombok:${lombokVersion}")
    annotationProcessor("org.projectlombok:lombok:${lombokVersion}")
    implementation("com.google.guava:guava:${guavaVersion}")
    testAnnotationProcessor("org.projectlombok:lombok:${lombokVersion}")
    testImplementation("org.projectlombok:lombok:${lombokVersion}")
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.postgresql:postgresql:${postgresVersion}")
    implementation("org.flywaydb:flyway-core:${flywayVersion}")
    implementation("com.alibaba:fastjson:${fastjsonVersion}")
    implementation("io.springfox:springfox-boot-starter:${springfoxVersion}")
    implementation("org.springframework.boot:spring-boot-starter-data-mongodb")
    implementation("org.mybatis.spring.boot:mybatis-spring-boot-starter:${mybatisVersion}")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    implementation("org.springframework.kafka:spring-kafka:2.7.6")
    testImplementation("org.scala-lang:scala-library:${scalaVersion}")
    testImplementation("org.springframework.boot:spring-boot-starter-actuator")
    testImplementation("org.springframework.boot:spring-boot-devtools")
    testImplementation("com.baomidou:mybatis-plus-generator:${generatorVersion}")
    testImplementation("org.apache.velocity:velocity-engine-core:${velocityVersion}")
}

tasks.register<Copy>("copyJarKafkaConsumer") {
    copy {
        from("build/libs/kafka-consumer-${minionsVersion}.jar"){
            rename("kafka-consumer-${minionsVersion}.jar", "kafka-consumer.jar")
        }
        into("$buildDir/../../project_files/libs")
    }
}

tasks.build {
    finalizedBy(tasks.getByName("copyJarKafkaConsumer"))
}

java {
    sourceCompatibility = JavaVersion.VERSION_11
    targetCompatibility = JavaVersion.VERSION_11
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
