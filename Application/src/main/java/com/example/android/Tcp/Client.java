package com.example.android.Tcp;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Matrix;

import java.io.*;
import java.net.Socket;

public class Client extends Socket{
    private final String SERVER_IP="10.110.8.236";
    private final int SERVER_PORT=8999;
    private Socket client;
    private DataOutputStream dos;
    private DataInputStream dis;

    public Client() throws IOException{
        this.client=new Socket(SERVER_IP,SERVER_PORT);
        System.out.println("======== Connect to server :: "+SERVER_IP+" ========");
    }

    public static byte [] compressImage(byte [] photo) {
        // Create Bitmap by byte[]
        Bitmap originBitmap = BitmapFactory.decodeByteArray(photo, 0, photo.length);

        // Resize the bitmap
        Matrix scaleMatrix = new Matrix();
        scaleMatrix.postScale(0.5f,0.5f);
        Bitmap resizeBmp = Bitmap.createBitmap(originBitmap,0,0,originBitmap.getWidth(),
                originBitmap.getHeight(),scaleMatrix,true);

        // Create byte[] by bitmap, using Bitmap.compress
        // -?- Strangely, Bitmap.compress seems to rotate 90 degree, so fix it first
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        Matrix rotateMatrix = new Matrix();
        rotateMatrix.setRotate(90);
        Bitmap rotateBmp = Bitmap.createBitmap(resizeBmp,0,0,resizeBmp.getWidth(),
                resizeBmp.getHeight(), rotateMatrix, false);
        rotateBmp.compress(Bitmap.CompressFormat.JPEG, 100, bos);
        byte[] bitmapBytes = bos.toByteArray();

        return bitmapBytes;
    }

    public byte[] sendFile(byte[] bytes) throws IOException {
        byte[] result = null;
        try {
            dos = new DataOutputStream(client.getOutputStream());

            // Compress image
            byte[] image = compressImage(bytes);

            // Begin transmission
            System.out.println("======== Begin Image Transmission ========");
            InputStream inputStream = new ByteArrayInputStream(image);
            byte[] inputPacket = new byte[1024];
            int length = 0;
            while((length = inputStream.read(inputPacket, 0, inputPacket.length)) != -1) {
                dos.write(inputPacket, 0, length);
                dos.flush();
            }
            client.shutdownOutput();
            System.out.println("======== Success Image Transmission ========");

            // Begin receiving
            dis = new DataInputStream(client.getInputStream());
            System.out.println("======== Begin Image Receiving ========");
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            byte[] outputPacket = new byte[1024];
            while ((length = dis.read(outputPacket, 0, outputPacket.length)) != -1) {
                baos.write(outputPacket, 0, length);
            }
            result=baos.toByteArray();
            System.out.println("======== Success Image Receiving ========");

        }catch(IOException e){
            e.printStackTrace();
            System.out.println("******** Error when Client sending message ********");
       }finally{
            client.close();
        }
        return result;
    }
}