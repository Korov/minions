plugins {
    id("org.jetbrains.kotlin.jvm")
    id("groovy")
    id("org.springframework.boot")
    id("com.thinkimi.gradle.MybatisGenerator")
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
    implementation("io.springfox:springfox-boot-starter:${springfoxVersion}")
    implementation("org.mybatis.spring.boot:mybatis-spring-boot-starter:${mybatisVersion}")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.spockframework:spock-core:${spockVersion}")
    testImplementation("org.spockframework:spock-spring:${spockVersion}")
    testImplementation("org.codehaus.groovy:groovy:${groovyVersion}")
    testImplementation("org.springframework.boot:spring-boot-starter-actuator")
    testImplementation("org.springframework.boot:spring-boot-devtools")
}

tasks.register<Copy>("copyJarDemo") {
    copy {
        from("build/libs/demo-${minionsVersion}.jar")
        into("$buildDir/../../project_files/libs/demo.jar")
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
        mybatisGenerator("org.mybatis.generator:mybatis-generator-core:${mybatisGeneratorVersion}")
        mybatisGenerator("org.postgresql:postgresql:${postgresVersion}")
    }
}

mybatisGenerator {
    verbose = true
    configFile = "src/main/resources/autogen/generatorConfig.xml"

    // optional, here is the override dependencies for the plugin or you can add other database dependencies.
    dependencies {
        mybatisGenerator("org.mybatis.generator:mybatis-generator-core:1.3.7")
        mybatisGenerator("org.postgresql:postgresql:${postgresVersion}")
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
    reports{
        junitXml.required.set(false)
        html.required.set(true)
    }
    finalizedBy(tasks.jacocoTestReport)  // report is always generated after tests run
}

tasks.jacocoTestReport {
    dependsOn(tasks.test)  // tests are required to run before generating the report
}
