package org.minions.demo.config;

import io.swagger.annotations.Api;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

/**
 * @author korov
 */
@Configuration
public class Swagger3Config {
    @Bean
    public Docket createRestApi(){
        return new Docket(DocumentationType.OAS_30)
                .apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.withClassAnnotation(Api.class))
                .paths(PathSelectors.any())
                .build();
    }

    //基本信息的配置，信息会在api文档上显示
    private static ApiInfo apiInfo(){
        return new ApiInfoBuilder()
                .title("demo")
                .description("demo接口文档")
                .contact(new Contact("Korov", "https://github.com/Korov", "korov9@163.com"))
                .version("1.0")
                .build();
    }
}
