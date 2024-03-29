package org.minions.common.utils;

import com.fasterxml.jackson.databind.JsonNode;
import lombok.extern.slf4j.Slf4j;
import okhttp3.*;
import org.minions.common.constant.Constant;

import java.util.concurrent.TimeUnit;

/**
 * 使用HTTP发送请求
 *
 * @author korov
 * @date 2020/10/3
 */
@Slf4j
public class HttpUtil {
    //http连接查询接口数据POST
    public static JsonNode postSpider(String host, int port, String project, String spider) {

        OkHttpClient okhttp = new OkHttpClient();
        okhttp.newBuilder().connectTimeout(10000L, TimeUnit.MILLISECONDS).readTimeout(50000, TimeUnit.MILLISECONDS).build();
        RequestBody requestBody = new FormBody.Builder()
                .add("project", project)
                .add("spider", spider).build();
        String url = String.format("http://%s:%s/schedule.json", host, port);
        //创建一个Request
        Request request = new Request.Builder().post(requestBody).url(url).build();
        JsonNode resultForJson = null;
        try (Response response = okhttp.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                log.error("post spider failed!");
            }
            String result = Constant.BLACK;
            ResponseBody body = response.body();
            if (body != null) {
                result = body.string();
            }
            resultForJson = JsonUtil.objectToNode(result, JsonUtil.SNAKE_CASE_MAPPER);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return resultForJson;
    }
}
