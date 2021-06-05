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
    id("org.jetbrains.kotlin.jvm") version "1.4.32"
    id("groovy")
}

dependencies {
    implementation("org.codehaus.groovy:groovy:3.0.7")
    implementation("org.projectlombok:lombok:${lombokVersion}")
    implementation("com.fasterxml.jackson.module:jackson-module-kotlin")
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.4.32")
    annotationProcessor("org.projectlombok:lombok:${lombokVersion}")
    implementation("com.alibaba:fastjson:${fastjsonVersion}")
    implementation("org.yaml:snakeyaml:${snakeyamlVersion}")
    implementation("com.squareup.okhttp3:okhttp")
    implementation("io.springfox:springfox-boot-starter:${swaggerVersion}")
    implementation("org.springframework.boot:spring-boot-starter-validation")
    implementation("org.springframework.boot:spring-boot-starter-logging")
    implementation("org.springframework.boot:spring-boot-starter-data-mongodb")
    implementation("com.google.guava:guava:30.1.1-jre")
    implementation("org.jetbrains.kotlin:kotlin-reflect:${kotlinVersion}")
    testImplementation("org.spekframework.spek2:spek-dsl-jvm:2.0.15")
    testImplementation("org.spekframework.spek2:spek-runner-junit5:2.0.15")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.junit.platform:junit-platform-launcher")
    testImplementation("org.junit.jupiter:junit-jupiter-engine")
    testCompile(platform("org.spockframework:spock-bom:2.0-M4-groovy-3.0"))
    testImplementation("org.spockframework:spock-core")
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
    effort.set(com.github.spotbugs.snom.Effort.MAX)
    tasks.spotbugsMain {
        ignoreFailures = true
        reports.create("html") {
            isEnabled = true
            destination = file("$buildDir/reports/spotbugs/main/spotbugs.html")
            setStylesheet("fancy-hist.xsl")
        }
    }

    /*tasks.spotbugsTest {
        ignoreFailures = true
        reports.create("html") {
            isEnabled = true
            destination = file("$buildDir/reports/spotbugs/test/spotbugs.html")
            setStylesheet("fancy-hist.xsl")
        }
    }*/
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

