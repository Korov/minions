package org.minions.demo

import com.baomidou.mybatisplus.generator.AutoGenerator
import com.baomidou.mybatisplus.generator.config.*
import com.baomidou.mybatisplus.generator.config.converts.PostgreSqlTypeConvert
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy
import com.baomidou.mybatisplus.generator.keywords.PostgreSqlKeyWordsHandler
import com.google.common.collect.ImmutableList
import org.junit.jupiter.api.Test

/**
 * @author zhu.lei
 * @date 2021-09-06 13:34
 */
class Generator {
    @Test
    void test() {
        AutoGenerator generator = new AutoGenerator()

        // 全局配置
        String projectPath = System.getProperty("user.dir")
        GlobalConfig gc = new GlobalConfig()
                .setOutputDir(projectPath + File.separator + ImmutableList.of("src", "main", "java").join(File.separator))
                .setFileOverride(true)
                .setAuthor("korov")
                .setOpen(false)
        generator.setGlobalConfig(gc)


        // 数据源配置
        DataSourceConfig dsc = new DataSourceConfig()
                .setUrl("jdbc:postgresql://localhost:5432/minions?currentSchema=demo")
                .setDriverName("org.postgresql.Driver")
                .setSchemaName("demo")
                .setUsername("minions")
                .setPassword("postgres")
                .setKeyWordsHandler(new PostgreSqlKeyWordsHandler())
                .setTypeConvert(new PostgreSqlTypeConvert())
        generator.setDataSource(dsc)


        // 配置模板
        TemplateConfig templateConfig = new TemplateConfig()
                .setService(null)
                .setServiceImpl(null)
                .setController(null)
                .setXml(null)
        generator.setTemplate(templateConfig)


        // 包配置
        PackageConfig pc = new PackageConfig()
                .setModuleName("demo")
                .setParent("org.minions")
        generator.setPackageInfo(pc)

        // 策略配置
        StrategyConfig strategy = new StrategyConfig()
                .setNaming(NamingStrategy.underline_to_camel)
                .setColumnNaming(NamingStrategy.underline_to_camel)
                .setInclude("demo")
                .setEntityColumnConstant(true)
        generator.setStrategy(strategy)
        generator.execute()
    }
}
