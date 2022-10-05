package org.minions.common.utils;

import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.concurrent.ConcurrentHashMap;

public class Demo {
    private static final Logger log = LoggerFactory.getLogger(Demo.class);

    @Test
    public void test1() {
        Map<Dto, String> map = new ConcurrentHashMap<>();
        for (int i = 0; i < 128; i++) {
            map.put(new Dto(i), String.valueOf(i));
            log.info("index:{}", i);
        }
        log.info("debug");
    }

    class Dto {
        private int key;

        public Dto(int key) {
            this.key = key;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Dto dto = (Dto) o;

            return Objects.equals(key, dto.key);
        }

        @Override
        public int hashCode() {
            return key < 5 ? 0 : 1;
        }
    }

    @Test
    public void test2() {
        int result = 32 >>> 2;
        log.info("result:{}", result);
    }
}
