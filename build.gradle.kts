import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

buildscript {
    extra.apply {
        set("springbootVersion", "2.7.7")
        set("postgresVersion","42.5.1")
        set("lombokVersion","1.18.24")
        set("groovyVersion","4.0.7")
        set("okhttpVersion","5.0.0-alpha.11")
        set("jacksonVersion","2.14.1")
        set("kotlinVersion","1.7.10")
        set("snakeyamlVersion","1.33")
        set("springKafkaVersion","3.0.1")
        set("guavaVersion","31.1-jre")
        set("flywayVersion","9.10.2")
        set("scalaVersion","3.2.1")
        set("mybatisVersion","3.0.1")
        set("springDocVersion","1.6.14")
        set("spek2Version","2.0.18")
        set("spockVersion","2.4-M1-groovy-4.0")
        set("minionsVersion","0.0.3-SNAPSHOT")
        set("generatorVersion","3.5.3.1")
        set("velocityVersion","2.3")
        set("mybatisPlusVersion","3.5.1")
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
        classpath("com.github.spotbugs.snom:spotbugs-gradle-plugin:5.0.13")
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${rootProject.extra.get("springbootVersion")}")
        classpath("io.spring.gradle:dependency-management-plugin:1.1.0")
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
        sourceCompatibility = JavaVersion.VERSION_17.toString()
        targetCompatibility = JavaVersion.VERSION_17.toString()
    }

    tasks.withType<KotlinCompile> {
        kotlinOptions.jvmTarget = JavaVersion.VERSION_17.toString()
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
            mavenBom("org.springframework.cloud:spring-cloud-dependencies:2021.0.4")
            mavenBom("com.alibaba.cloud:spring-cloud-alibaba-dependencies:2021.0.4.0")
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