package org.minions.demo.service.impl


import org.minions.demo.DemoApplicationTest
import org.minions.demo.service.DemoService
import org.springframework.beans.factory.annotation.Autowired

class DemoServiceImplTest extends DemoApplicationTest {
    private DemoService demoService

    @Autowired
    void setDemoService(DemoService demoService) {
        this.demoService = demoService
    }

    def "test1"() {
        expect: "test"
        demoService.testTransaction("test1")
    }
}
