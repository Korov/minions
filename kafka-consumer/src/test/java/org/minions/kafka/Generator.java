package org.minions.kafka;

import com.baomidou.mybatisplus.generator.AutoGenerator;
import com.baomidou.mybatisplus.generator.config.*;
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;
import com.google.common.base.Joiner;
import com.google.common.collect.ImmutableList;
import org.junit.jupiter.api.Test;

import java.io.File;

public class Generator {
    @Test
    void test() {
        AutoGenerator generator = new AutoGenerator();

        // 全局配置
        GlobalConfig gc = new GlobalConfig();
        String projectPath = System.getProperty("user.dir");
        gc.setOutputDir(projectPath + File.separator + Joiner.on(File.separator).join(ImmutableList.of("src", "main", "java")));
        gc.setFileOverride(true);
        gc.setAuthor("korov");
        gc.setOpen(false);
        generator.setGlobalConfig(gc);

        // 数据源配置
        DataSourceConfig dsc = new DataSourceConfig();
        dsc.setUrl("jdbc:postgresql://localhost:5432/minions?currentSchema=kafka");
        dsc.setDriverName("org.postgresql.Driver");
        dsc.setSchemaName("kafka");
        dsc.setUsername("minions");
        dsc.setPassword("postgres");
        generator.setDataSource(dsc);

        // 配置模板
        TemplateConfig templateConfig = new TemplateConfig();
        templateConfig.setService(null);
        templateConfig.setServiceImpl(null);
        templateConfig.setController(null);
        templateConfig.setXml(null);
        generator.setTemplate(templateConfig);

        // 包配置
        PackageConfig pc = new PackageConfig();
        pc.setModuleName("kafka-consumer");
        pc.setParent("org.minions.kafka");
        generator.setPackageInfo(pc);

        // 策略配置
        StrategyConfig strategy = new StrategyConfig();
        strategy.setNaming(NamingStrategy.underline_to_camel);
        strategy.setColumnNaming(NamingStrategy.underline_to_camel);
        strategy.setEntityColumnConstant(true);
        strategy.setInclude("hero_infos", "hero_weapon");
        generator.setStrategy(strategy);
        generator.execute();
    }
}
