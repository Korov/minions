package org.minions.kafka;

import com.baomidou.mybatisplus.generator.AutoGenerator;
import com.baomidou.mybatisplus.generator.config.*;
import com.google.common.base.Joiner;
import com.google.common.collect.ImmutableList;
import org.junit.jupiter.api.Test;

import java.io.File;

public class Generator {
    @Test
    void test() {
        // 全局配置
        String projectPath = System.getProperty("user.dir");
        GlobalConfig gc = new GlobalConfig.Builder()
                .outputDir(projectPath + File.separator + Joiner.on(File.separator).join(ImmutableList.of("src", "main", "java")))
                .author("korov")
                .disableOpenDir()
                .build();

        // 数据源配置
        String url = "jdbc:postgresql://localhost:5432/minions?currentSchema=kafka";
        String username = "minions";
        String password = "postgres";
        DataSourceConfig dsc = new DataSourceConfig.Builder(url, username, password)
                .schema("kafka").build();

        AutoGenerator generator = new AutoGenerator(dsc);
        generator.global(gc);


        // 配置模板
        TemplateConfig templateConfig = new TemplateConfig.Builder().build();
        generator.template(templateConfig);


        // 包配置
        PackageConfig pc = new PackageConfig.Builder().moduleName("kafka-consumer").parent("org.minions.kafka").build();
        generator.packageInfo(pc);

        // 策略配置
        StrategyConfig strategy = new StrategyConfig.Builder()
                .addInclude("hero_infos", "hero_weapon")
                .build();
        generator.strategy(strategy);
        generator.execute();
    }
}
