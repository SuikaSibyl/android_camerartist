package com.example.android.camera2basic;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.example.android.camera2basic.R;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);

        Button btnStylize = findViewById(R.id.btnStylize);
        btnStylize.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                sendMessage(v);
            }
        });
    }

    public void sendMessage(View view) {
        Intent intent = new Intent(this, CameraActivity.class);
        startActivity(intent);
    }
}