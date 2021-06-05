buildscript {
    extra.apply {
        set("springbootVersion", "2.4.6")
        set("springCloudVersion", "2020.0.3")
        set("swaggerVersion", "3.0.0")
        set("okhttpVersion", "4.9.1")
        set("lombokVersion", "1.18.18")
        set("fastjsonVersion", "1.2.75")
        set("snakeyamlVersion", "1.28")
        set("postgresVersion", "42.2.19")
        set("mybatisVersion", "2.1.4")
        set("spotbugsVersion", "4.7.1")
        set("dependencyManagementVersion", "1.0.11.RELEASE")
        set("flywayVersion", "7.7.0")
        set("scalaLibraryVersion", "2.13.5")
        set("kotlinVersion", "1.4.32")
    }
    val springbootVersion: String by rootProject.extra

    repositories {
        mavenLocal()
        maven {
            setUrl("https://maven.aliyun.com/repository/central")
        }
        maven {
            setUrl("https://maven.aliyun.com/repository/gradle-plugin")
        }
    }

    dependencies {
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springbootVersion}")
        classpath("gradle.plugin.com.github.spotbugs.snom:spotbugs-gradle-plugin:4.7.1")
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springbootVersion}")
        classpath("io.spring.gradle:dependency-management-plugin:1.0.11.RELEASE")
        classpath("gradle.plugin.com.thinkimi.gradle:mybatis-generator-plugin:2.2")
    }
}

//所有项目共用的设置
allprojects {
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
    group = "org.minions"
    version = "0.0.1-SNAPSHOT"

    repositories {
        mavenLocal()
        maven {
            setUrl("https://maven.aliyun.com/repository/central")
        }
        maven {
            setUrl("https://maven.aliyun.com/repository/gradle-plugin")
        }
    }

    // 此插件来实现类似maven中的dependencyManagement功能
    apply {
        plugin("java")
        plugin("idea")
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
            mavenBom("org.springframework.cloud:spring-cloud-dependencies:${springCloudVersion}")
            mavenBom("org.springframework.boot:spring-boot-dependencies:${springbootVersion}")
        }
        dependencies {
            dependency("com.squareup.okhttp3:okhttp:4.9.1")
        }
    }
}

subprojects {
    apply {
        plugin("jacoco")
        plugin("com.github.spotbugs")
    }
}