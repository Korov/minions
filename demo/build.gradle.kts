plugins {
    id("org.jetbrains.kotlin.jvm")
    id("groovy")
    id("idea")
    id("org.springframework.boot")
}

val postgresVersion: String by rootProject.extra
val mybatisGeneratorVersion: String by rootProject.extra
val lombokVersion: String by rootProject.extra
val groovyVersion: String by rootProject.extra
val springbootVersion: String by rootProject.extra
val fastjsonVersion: String by rootProject.extra
val flywayVersion: String by rootProject.extra
val mybatisVersion: String by rootProject.extra
val springfoxVersion: String by rootProject.extra
val spockVersion: String by rootProject.extra
val minionsVersion: String by rootProject.extra
val generatorVersion: String by rootProject.extra
val velocityVersion: String by rootProject.extra
val mybatisPlusVersion: String by rootProject.extra

dependencies {
    implementation(project(":common"))
    implementation("org.projectlombok:lombok:${lombokVersion}")
    annotationProcessor("org.projectlombok:lombok:${lombokVersion}")
    implementation("com.alibaba.cloud:spring-cloud-starter-alibaba-nacos-discovery")
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.springframework.boot:spring-boot-starter-actuator")
    implementation("org.springframework.boot:spring-boot-devtools")
    implementation("org.postgresql:postgresql:${postgresVersion}")
    implementation("org.flywaydb:flyway-core:${flywayVersion}")
    implementation("com.alibaba:fastjson:${fastjsonVersion}")
    implementation("io.springfox:springfox-boot-starter:${springfoxVersion}")
    implementation("org.mybatis.spring.boot:mybatis-spring-boot-starter:${mybatisVersion}")
    implementation("com.baomidou:mybatis-plus-boot-starter:${mybatisPlusVersion}")
    testAnnotationProcessor("org.projectlombok:lombok:${lombokVersion}")
    testImplementation("org.projectlombok:lombok:${lombokVersion}")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.spockframework:spock-core:${spockVersion}")
    testImplementation("org.spockframework:spock-spring:${spockVersion}")
    testImplementation("org.codehaus.groovy:groovy:${groovyVersion}")
    testImplementation("com.baomidou:mybatis-plus-generator:${generatorVersion}")
    testImplementation("org.apache.velocity:velocity-engine-core:${velocityVersion}")
}

tasks.register<Copy>("copyJarDemo") {
    copy {
        from("build/libs/demo-${minionsVersion}.jar") {
            rename("demo-${minionsVersion}.jar", "demo.jar")
        }
        into("$buildDir/../../project_files/libs")
    }
}

tasks.build {
    finalizedBy(tasks.getByName("copyJarDemo"))
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
