package com.example.android.camera2basic;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;

public class Receiver extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_receiver);

        ImageView imageView = findViewById(R.id.ivReturn);

        Intent intent = getIntent();
        byte[] image = intent.getByteArrayExtra("image");
        Bitmap myBitmap = BitmapFactory.decodeByteArray(image, 0, image.length);

        imageView.setImageBitmap(myBitmap);
    }
}
