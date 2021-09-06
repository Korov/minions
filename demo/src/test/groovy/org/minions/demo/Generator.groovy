package org.minions.demo

import com.baomidou.mybatisplus.generator.AutoGenerator
import com.baomidou.mybatisplus.generator.config.DataSourceConfig
import com.baomidou.mybatisplus.generator.config.GlobalConfig
import com.baomidou.mybatisplus.generator.config.PackageConfig
import com.baomidou.mybatisplus.generator.config.StrategyConfig
import com.baomidou.mybatisplus.generator.engine.FreemarkerTemplateEngine
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
        GlobalConfig gc = new GlobalConfig()
        String projectPath = System.getProperty("user.dir")
        gc.setOutputDir(projectPath + "/demo/src/main/java")
        gc.setAuthor("korov")
        gc.setOpen(false)
        generator.setGlobalConfig(gc)

        // 数据源配置
        DataSourceConfig dsc = new DataSourceConfig()
        dsc.setUrl("jdbc:postgresql://localhost:5432/minions?currentSchema=demo")
        dsc.setDriverName("org.postgresql.Driver")
        dsc.setUsername("minions")
        dsc.setPassword("postgres")
        generator.setDataSource(dsc)

        // 包配置
        PackageConfig pc = new PackageConfig()
        pc.setModuleName(scanner("demo"))
        pc.setParent("org.minions.demo")
        generator.setPackageInfo(pc)

        // 策略配置
        StrategyConfig strategy = new StrategyConfig()
        strategy.setNaming(NamingStrategy.underline_to_camel)
        strategy.setColumnNaming(NamingStrategy.underline_to_camel)
        strategy.setInclude("demo")
        generator.setStrategy(strategy)
        generator.execute()
    }
}
