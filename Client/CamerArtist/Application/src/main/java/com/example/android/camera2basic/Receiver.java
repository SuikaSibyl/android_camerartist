package com.example.android.camera2basic;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;

import java.io.File;

public class Receiver extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_receiver);

        ImageView imageView = findViewById(R.id.ivReturn);

        try
        {
            System.out.println("enter Receiver");
            Bitmap bitmap = null;
            Intent intent = getIntent();
//            byte[] image = intent.getByteArrayExtra("image");
//            Bitmap myBitmap = BitmapFactory.decodeByteArray(image, 0, image.length);
            String path = getExternalFilesDir(null)+"/result.jpg";
            File file = new File(path);
            if(file.exists())
            {
                bitmap = BitmapFactory.decodeFile(path);
            }
            imageView.setImageBitmap(bitmap);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
