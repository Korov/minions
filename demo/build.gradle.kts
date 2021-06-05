val springbootVersion: String by rootProject.extra
val springCloudVersion: String by rootProject.extra
val swaggerVersion: String by rootProject.extra
val okhttpVersion: String by rootProject.extra
val lombokVersion: String by rootProject.extra
val fastjsonVersion: String by rootProject.extra
val snakeyamlVersion: String by rootProject.extra
val postgresVersion: String by rootProject.extra
val mybatisVersion: String by rootProject.extra
val spotbugsVersion: String by rootProject.extra
val dependencyManagementVersion: String by rootProject.extra
val flywayVersion: String by rootProject.extra
val scalaLibraryVersion: String by rootProject.extra
val kotlinVersion: String by rootProject.extra

plugins {
    id("org.jetbrains.kotlin.jvm")
    id("groovy")
    id("org.springframework.boot")
    id("com.thinkimi.gradle.MybatisGenerator")
}

dependencies {
    implementation(project(":common"))
    implementation("org.projectlombok:lombok:${lombokVersion}")
    annotationProcessor("org.projectlombok:lombok:${lombokVersion}")
    testAnnotationProcessor("org.projectlombok:lombok:${lombokVersion}")
    testImplementation("org.projectlombok:lombok:${lombokVersion}")
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.postgresql:postgresql:${postgresVersion}")
    implementation("org.flywaydb:flyway-core:${flywayVersion}")
    implementation("com.alibaba:fastjson:${fastjsonVersion}")
    implementation("io.springfox:springfox-boot-starter:${swaggerVersion}")
    implementation("org.mybatis.spring.boot:mybatis-spring-boot-starter:${mybatisVersion}")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.spockframework:spock-core:2.0-M4-groovy-3.0")
    testImplementation("org.spockframework:spock-spring:2.0-M4-groovy-3.0")
    testImplementation("org.codehaus.groovy:groovy:3.0.7")
    testImplementation("org.springframework.boot:spring-boot-starter-actuator")
    testImplementation("org.springframework.boot:spring-boot-devtools")
}

tasks.register<Copy>("copyJarDemo") {
    copy {
        from("build/libs/demo-0.0.1-SNAPSHOT.jar")
        into("$buildDir/../../project_files/libs")
    }
}

tasks.build {
    finalizedBy(tasks.getByName("copyJarDemo"))
}

configurations {
    mybatisGenerator
}

mybatisGenerator {
    verbose = true
    configFile = "src/main/resources/autogen/generatorConfig.xml"

    // optional, here is the override dependencies for the plugin or you can add other database dependencies.
    dependencies {
        mybatisGenerator("org.mybatis.generator:mybatis-generator-core:1.3.7")
        mybatisGenerator("org.postgresql:postgresql:42.2.6")
    }
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
    finalizedBy(tasks.jacocoTestReport)  // report is always generated after tests run
}

tasks.jacocoTestReport {
    dependsOn(tasks.test)  // tests are required to run before generating the report
}
