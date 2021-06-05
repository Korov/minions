plugins {
    id("org.jetbrains.kotlin.jvm")
    id("groovy")
}

dependencies {
    implementation("org.codehaus.groovy:groovy")
    implementation("org.projectlombok:lombok:")
    implementation("com.fasterxml.jackson.module:jackson-module-kotlin")
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")
    annotationProcessor("org.projectlombok:lombok")
    implementation("com.alibaba:fastjson")
    implementation("org.yaml:snakeyaml")
    implementation("com.squareup.okhttp3:okhttp")
    implementation("io.springfox:springfox-boot-starter")
    implementation("org.springframework.boot:spring-boot-starter-validation")
    implementation("org.springframework.boot:spring-boot-starter-data-mongodb")
    implementation("com.google.guava:guava")
    implementation("org.jetbrains.kotlin:kotlin-reflect")
    testImplementation("org.spekframework.spek2:spek-dsl-jvm")
    testImplementation("org.spekframework.spek2:spek-runner-junit5")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.junit.platform:junit-platform-launcher")
    testImplementation("org.junit.jupiter:junit-jupiter-engine")
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
    finalizedBy(tasks.jacocoTestReport)  // report is always generated after tests run
}

tasks.jacocoTestReport {
    dependsOn(tasks.test)  // tests are required to run before generating the report
}

