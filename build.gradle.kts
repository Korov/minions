buildscript {
    extra.apply {
        set("springbootVersion", "2.5.3")
    }
    val springbootVersion: String by rootProject.extra

    repositories {
        mavenLocal()
        maven {
            url = uri("https://maven.aliyun.com/repository/central")
        }
        maven {
            url = uri("https://maven.aliyun.com/repository/gradle-plugin")
        }
    }

    dependencies {
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springbootVersion}")
        classpath("gradle.plugin.com.github.spotbugs.snom:spotbugs-gradle-plugin:4.7.1")
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springbootVersion}")
        classpath("io.spring.gradle:dependency-management-plugin:1.0.11.RELEASE")
        classpath("gradle.plugin.com.thinkimi.gradle:mybatis-generator-plugin:2.2")
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.4.32")
    }
}

//所有项目共用的设置
allprojects {
    val springbootVersion: String by rootProject.extra
    group = "org.minions"
    version = "0.0.1-SNAPSHOT"

    repositories {
        mavenLocal()
        maven {
            url = uri("https://maven.aliyun.com/repository/central")
        }
        maven {
            url = uri("https://maven.aliyun.com/repository/gradle-plugin")
        }
    }

    apply {
        plugin("java")
        plugin("idea")
        // 此插件来实现类似maven中的dependencyManagement功能
        plugin("io.spring.dependency-management")
    }

    tasks.withType<JavaCompile> {
        options.encoding = "UTF-8"
        sourceCompatibility = "11"
    }

    tasks.withType<Test> {
        systemProperty("file.encoding", "UTF-8")
    }

    tasks.withType<Javadoc> {
        options.encoding = "UTF-8"
    }

    // io.spring.dependency-management插件的功能
    the<io.spring.gradle.dependencymanagement.dsl.DependencyManagementExtension>().apply {
        imports {
            // mavenBom(org.springframework.boot.gradle.plugin.SpringBootPlugin.BOM_COORDINATES)
            mavenBom("org.springframework.cloud:spring-cloud-dependencies:2020.0.3")
            mavenBom("org.springframework.boot:spring-boot-dependencies:${springbootVersion}")
            mavenBom("org.spockframework:spock-bom:2.0-groovy-3.0")
            mavenBom("org.junit:junit-bom:5.7.2")
        }
        dependencies {
            dependency("com.squareup.okhttp3:okhttp:4.9.1")
            dependency("org.codehaus.groovy:groovy-all:3.0.7")
            dependency("org.projectlombok:lombok:1.18.18")
            dependency("com.fasterxml.jackson.module:jackson-module-kotlin:2.12.3")
            dependency("org.jetbrains.kotlin:kotlin-stdlib':1.5.21")
            dependency("com.alibaba:fastjson:1.2.75")
            dependency("org.yaml:snakeyaml:1.28")
            dependency("io.springfox:springfox-boot-starter:3.0.0")
            dependency("com.google.guava:guava:30.1.1-jre")
            dependency("org.postgresql:postgresql:42.2.19")
            dependency("org.flywaydb:flyway-core:7.7.0")
            dependency("org.scala-lang:scala-library:2.13.5")
            dependency("org.mybatis.spring.boot:mybatis-spring-boot-starter:2.1.4")
            dependency("org.jetbrains.kotlin:kotlin-reflect:1.5.21")
            dependency("org.spekframework.spek2:spek-dsl-jvm:2.0.15")
            dependency("org.spekframework.spek2:spek-runner-junit5:2.0.15")
            dependency("com.baomidou:mybatis-plus-boot-starter:3.4.3.1")
        }
    }
}

subprojects {
    apply {
        plugin("jacoco")
        plugin("com.github.spotbugs")
    }
}