plugins {
    id("org.jetbrains.kotlin.jvm")
    id("groovy")
    id("idea")
}

val lombokVersion: String by rootProject.extra
val groovyVersion: String by rootProject.extra
val okhttpVersion: String by rootProject.extra
val jacksonVersion: String by rootProject.extra
val kotlinVersion: String by rootProject.extra
val fastjsonVersion: String by rootProject.extra
val snakeyamlVersion: String by rootProject.extra
val guavaVersion: String by rootProject.extra
val springfoxVersion: String by rootProject.extra
val spek2Version: String by rootProject.extra
val spockVersion: String by rootProject.extra

dependencies {
    implementation("org.projectlombok:lombok:${lombokVersion}")
    annotationProcessor("org.projectlombok:lombok:${lombokVersion}")
    implementation("com.fasterxml.jackson.module:jackson-module-kotlin:${jacksonVersion}")
    implementation("org.jetbrains.kotlin:kotlin-stdlib:${kotlinVersion}")
    implementation("org.jetbrains.kotlin:kotlin-stdlib-common:${kotlinVersion}")
    implementation("com.alibaba:fastjson:${fastjsonVersion}")
    implementation("org.yaml:snakeyaml:${snakeyamlVersion}")
    implementation("com.squareup.okhttp3:okhttp:${okhttpVersion}")
    implementation("io.springfox:springfox-boot-starter:${springfoxVersion}")
    implementation("org.springframework.boot:spring-boot-starter-validation")
    implementation("org.springframework.boot:spring-boot-starter-data-mongodb")
    implementation("com.google.guava:guava:${guavaVersion}")
    implementation("org.jetbrains.kotlin:kotlin-reflect:${kotlinVersion}")
    testImplementation("org.codehaus.groovy:groovy:${groovyVersion}")
    testImplementation("org.spekframework.spek2:spek-dsl-jvm:${spek2Version}")
    testImplementation("org.spekframework.spek2:spek-runner-junit5:${spek2Version}")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.spockframework:spock-core:${spockVersion}")
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
        reports.create("html") {
            isEnabled = true
            destination = file("$buildDir/reports/spotbugs/main/spotbugs.html")
            setStylesheet("fancy-hist.xsl")
        }
    }
}

tasks.test {
    useJUnitPlatform {
        includeEngines("junit-jupiter", "spek2")
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

