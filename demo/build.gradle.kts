plugins {
    id("org.jetbrains.kotlin.jvm")
    id("groovy")
    id("idea")
    id("org.springframework.boot")
}

dependencies {
    implementation(project(":common"))
    implementation("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    annotationProcessor("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    implementation("com.alibaba.cloud:spring-cloud-starter-alibaba-nacos-discovery")
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.springframework.boot:spring-boot-starter-actuator")
    implementation("org.springframework.boot:spring-boot-devtools")
    implementation("org.postgresql:postgresql:${rootProject.extra.get("postgresVersion")}")
    implementation("org.flywaydb:flyway-core:${rootProject.extra.get("flywayVersion")}")
    implementation("org.springdoc:springdoc-openapi-ui:${rootProject.extra.get("springDocVersion")}")
    implementation("org.mybatis.spring.boot:mybatis-spring-boot-starter:${rootProject.extra.get("mybatisVersion")}")
    implementation("com.baomidou:mybatis-plus-boot-starter:${rootProject.extra.get("mybatisPlusVersion")}")
    testAnnotationProcessor("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    testImplementation("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.spockframework:spock-core:${rootProject.extra.get("spockVersion")}")
    testImplementation("org.spockframework:spock-spring:${rootProject.extra.get("spockVersion")}")
    testImplementation("org.codehaus.groovy:groovy:${rootProject.extra.get("groovyVersion")}")
    testImplementation("com.baomidou:mybatis-plus-generator:${rootProject.extra.get("generatorVersion")}")
    testImplementation("org.apache.velocity:velocity-engine-core:${rootProject.extra.get("velocityVersion")}")
}

tasks.register<Copy>("copyJarDemo") {
    copy {
        from("build/libs/demo-${rootProject.extra.get("minionsVersion")}.jar") {
            rename("demo-${rootProject.extra.get("minionsVersion")}.jar", "demo.jar")
        }
        into("$buildDir/../../project_files/libs")
    }
}

tasks.build {
    finalizedBy(tasks.getByName("copyJarDemo"))
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
            enabled = true
            outputLocation.set(file("$buildDir/reports/spotbugs/main/spotbugs.html"))
            setStylesheet("fancy-hist.xsl")
        }
    }

    tasks.spotbugsTest {
        reports.create("html") {
            enabled = true
            outputLocation.set(file("$buildDir/reports/spotbugs/test/spotbugs.html"))
            setStylesheet("fancy-hist.xsl")
        }
    }
}

tasks.test {
    useJUnitPlatform {
        includeEngines("junit-jupiter", "spock")
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
