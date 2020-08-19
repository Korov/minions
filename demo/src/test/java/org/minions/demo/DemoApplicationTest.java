package org.minions.demo;

import org.junit.jupiter.api.Test;

public class DemoApplicationTest extends TestAnnotation {
    @Test
    public void loadContext() {
        System.out.println("Application start success!");
    }
}