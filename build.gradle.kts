buildscript {
    extra.apply {
        set("springbootVersion", "2.4.6")
        set("postgresVersion","42.2.23")
        set("mybatisGeneratorVersion","1.4.0")
        set("lombokVersion","1.18.20")
        set("groovyVersion","3.0.8")
        set("okhttpVersion","4.9.1")
        set("jacksonVersion","2.12.5")
        set("kotlinVersion","1.5.21")
        set("snakeyamlVersion","1.29")
        set("guavaVersion","30.1.1-jre")
        set("flywayVersion","7.7.0")
        set("scalaVersion","2.13.5")
        set("mybatisVersion","2.1.4")
        set("springfoxVersion","3.0.0")
        set("spek2Version","2.0.15")
        set("spockVersion","2.0-groovy-3.0")
        set("junitVersion","5.7.2")
        set("minionsVersion","0.0.3-SNAPSHOT")
        set("generatorVersion","3.4.1")
        set("velocityVersion","2.3")
        set("mybatisPlusVersion","3.4.3.3")
    }

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
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${rootProject.extra.get("springbootVersion")}")
        classpath("gradle.plugin.com.github.spotbugs.snom:spotbugs-gradle-plugin:4.7.1")
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${rootProject.extra.get("springbootVersion")}")
        classpath("io.spring.gradle:dependency-management-plugin:1.0.11.RELEASE")
        classpath("gradle.plugin.com.thinkimi.gradle:mybatis-generator-plugin:2.3")
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:${rootProject.extra.get("kotlinVersion")}")
    }
}

//所有项目共用的设置
allprojects {

    group = "org.minions"
    version = rootProject.extra.get("minionsVersion")!!

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
        sourceCompatibility = "17"
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
            mavenBom("org.springframework.cloud:spring-cloud-dependencies:2020.0.3")
            mavenBom("com.alibaba.cloud:spring-cloud-alibaba-dependencies:2020.0.RC1")
            mavenBom("org.springframework.boot:spring-boot-dependencies:${rootProject.extra.get("springbootVersion")}")
        }
    }
}

subprojects {
    apply {
        plugin("jacoco")
        plugin("com.github.spotbugs")
    }
}