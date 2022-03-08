plugins {
    id("org.jetbrains.kotlin.jvm")
    id("groovy")
    id("idea")
}

dependencies {
    implementation("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    annotationProcessor("org.projectlombok:lombok:${rootProject.extra.get("lombokVersion")}")
    implementation("com.fasterxml.jackson.module:jackson-module-kotlin:${rootProject.extra.get("jacksonVersion")}")
    implementation("org.jetbrains.kotlin:kotlin-stdlib:${rootProject.extra.get("kotlinVersion")}")
    implementation("org.jetbrains.kotlin:kotlin-stdlib-common:${rootProject.extra.get("kotlinVersion")}")
    implementation("org.yaml:snakeyaml:${rootProject.extra.get("snakeyamlVersion")}")
    implementation("com.squareup.okhttp3:okhttp:${rootProject.extra.get("okhttpVersion")}")
    implementation("io.springfox:springfox-boot-starter:${rootProject.extra.get("springfoxVersion")}")
    implementation("org.springframework.boot:spring-boot-starter-validation")
    implementation("org.springframework.boot:spring-boot-starter-data-mongodb")
    implementation("com.google.guava:guava:${rootProject.extra.get("guavaVersion")}")
    implementation("org.jetbrains.kotlin:kotlin-reflect:${rootProject.extra.get("kotlinVersion")}")
    implementation("com.baomidou:mybatis-plus-annotation:${rootProject.extra.get("mybatisPlusVersion")}")
    testImplementation("org.codehaus.groovy:groovy:${rootProject.extra.get("groovyVersion")}")
    testImplementation("org.spekframework.spek2:spek-dsl-jvm:${rootProject.extra.get("spek2Version")}")
    testImplementation("org.spekframework.spek2:spek-runner-junit5:${rootProject.extra.get("spek2Version")}")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.spockframework:spock-core:${rootProject.extra.get("spockVersion")}")
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

