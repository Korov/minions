package org.minions.common.utils;

import com.alibaba.fastjson.JSONObject;
import okhttp3.*;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

/**
 * 使用HTTP发送请求
 *
 * @author korov
 * @date 2020/10/3
 */
public class HttpUtil {
    //http连接查询接口数据POST
    public static JSONObject postSpider(String host, int port, String project, String spider) {

        OkHttpClient okhttp = new OkHttpClient();
        okhttp.newBuilder().connectTimeout(10000L, TimeUnit.MILLISECONDS).readTimeout(50000, TimeUnit.MILLISECONDS).build();
        RequestBody requestBody = new FormBody.Builder()
                .add("project", project)
                .add("spider", spider).build();
        String url = String.format("http://%s:%s/schedule.json", host, port);
        //创建一个Request
        Request request = new Request.Builder().post(requestBody).url(url).build();
        JSONObject resultForJson = null;
        try (Response response = okhttp.newCall(request).execute()){
            if (!response.isSuccessful()) {
                throw new IOException("unexpected code.." + response);
            }
            String result = response.body().string();
            resultForJson = JSONObject.parseObject(result);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return resultForJson;
    }
}
