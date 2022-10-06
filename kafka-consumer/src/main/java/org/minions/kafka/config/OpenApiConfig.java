package org.minions.kafka.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author korov
 */
@Configuration
public class OpenApiConfig {
    @Bean
    public OpenAPI createRestApi() {
        return new OpenAPI()
                .info(apiInfo());
    }

    //基本信息的配置，信息会在api文档上显示
    private static Info apiInfo() {
        Contact contact = new Contact();
        contact.setName("Korov");
        contact.setEmail("korov9@163.com");
        contact.setUrl("https://github.com/Korov");
        return new Info()
                .title("minions接口文档")
                .description("基于最新技术打造的数据收集平台")
                .contact(contact)
                .version("1.0");
    }
}
