package com.splo2t.safe_forklift;
import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.content.Intent;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;


import java.util.ArrayList;

import app.akexorcist.bluetotohspp.library.BluetoothSPP;
import app.akexorcist.bluetotohspp.library.BluetoothState;
import app.akexorcist.bluetotohspp.library.DeviceList;
import tk.splo2t.lab.R;

public class MainActivity extends AppCompatActivity {

    private BluetoothSPP bt;

    ImageView[] imgView = new ImageView[18];
    Button btnConnect;
    //TextView view;
    int[] prevData = new int[5];
    ArrayList<Integer> ledData = new ArrayList<>();
    private static Handler mHandler ;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bt = new BluetoothSPP(this); //Initializing
        ledData.add(-1);


        mHandler = new Handler() {
            @Override
            public void handleMessage(Message msg) {
                for(int i = 0; i < 18; i++){
                    imgView[i].setImageResource(R.color.white);
                }
                for(int i = 0; i < ledData.size(); i++){
                    if(ledData.get(i) < 0){
                        continue;
                    }
                    imgView[ledData.get(i)].setImageResource(R.color.black);
                }
                ledData.clear();
            }
        } ;


        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {

                    try {
                        Thread.sleep(250);
                    } catch (Exception e) {
                        e.printStackTrace() ;
                    }

                    mHandler.sendEmptyMessage(0) ;
                }
            }

        }).start();



        //view = findViewById(R.id.textView);
        imgView[0] = findViewById(R.id.imageView0);
        imgView[1] = findViewById(R.id.imageView1);
        imgView[2] = findViewById(R.id.imageView2);
        imgView[3] = findViewById(R.id.imageView3);
        imgView[4] = findViewById(R.id.imageView4);
        imgView[5] = findViewById(R.id.imageView5);
        imgView[6] = findViewById(R.id.imageView6);
        imgView[7] = findViewById(R.id.imageView7);
        imgView[8] = findViewById(R.id.imageView8);
        imgView[9] = findViewById(R.id.imageView9);
        imgView[10] = findViewById(R.id.imageView10);
        imgView[11] = findViewById(R.id.imageView11);
        imgView[12] = findViewById(R.id.imageView12);
        imgView[13] = findViewById(R.id.imageView13);
        imgView[14] = findViewById(R.id.imageView14);
        imgView[15] = findViewById(R.id.imageView15);
        imgView[16] = findViewById(R.id.imageView16);
        imgView[17] = findViewById(R.id.imageView17);


        btnConnect = findViewById(R.id.btnConnect); //연결시도
        //imgView53.setImageResource(R.color.white);

        if (!bt.isBluetoothAvailable()) { //블루투스 사용 불가
            Toast.makeText(getApplicationContext()
                    , "Bluetooth is not available"
                    , Toast.LENGTH_SHORT).show();
            finish();
        }

        bt.setOnDataReceivedListener(new BluetoothSPP.OnDataReceivedListener() {

            public void onDataReceived(byte[] data, String message) {
                //view.setText(message.replace("\n","b"));
                String[] tempDataArray = message.replace("\n","").split("#");
                int distanceHigh = 55;
                int sector = 0;
                if (tempDataArray.length < 5){
                    return;
                }
                //ledOff(R.color.white);
                for(int i = 1; i < 5; i++){
                    String temp = tempDataArray[i];
                    int parseData = Integer.parseInt(tempDataArray[i]);
                    if(Math.abs(prevData[i]-parseData) >= 8){
                        prevData[i] = parseData;
                        continue;
                    }
                    prevData[i] = parseData;
                    if(Integer.parseInt(temp) < distanceHigh){
                        if (i == 1){ //F
                            sector = 360-Integer.parseInt(tempDataArray[0]);
                        }
                        else if (i == 2) { //L
                            sector = (270-(Integer.parseInt(tempDataArray[0])))%360;
                            //view.setText("L:"+String.valueOf(sector));
                        }
                        else if (i == 3) { //R
                            sector = (450-(Integer.parseInt(tempDataArray[0])))%360;
                        }
                        else if (i == 4) { //B
                            sector = (180-(Integer.parseInt(tempDataArray[0])))%360;
                        }
                        if(sector == 360){
                            sector -= 1;
                        }
                        //int inputSector = (sector-18+360)%360/36;
                        ledData.add(sector/20);
                        //ledOn((sector/20));
                    }

                }
            }

            void ledOff(int color){
                for(int i = 0; i < 18; i++){
                    imgView[i].setImageResource(color);
                }
            }

            void ledOn(int led){
                imgView[led].setImageResource(R.color.black);
            }
        });


        bt.setBluetoothConnectionListener(new BluetoothSPP.BluetoothConnectionListener() { //연결됐을 때
            public void onDeviceConnected(String name, String address) {
                Toast.makeText(getApplicationContext()
                        , "Connected to " + name + "\n" + address
                        , Toast.LENGTH_SHORT).show();
                //btnConnect.setBackgroundColor(getResources().getColor(R.color.black));
            }

            public void onDeviceDisconnected() { //연결해제
                Toast.makeText(getApplicationContext()
                        , "Connection lost", Toast.LENGTH_SHORT).show();
                //btnConnect.setBackgroundColor(getResources().getColor(R.color.white));
            }

            public void onDeviceConnectionFailed() { //연결실패
                Toast.makeText(getApplicationContext()
                        , "Unable to connect", Toast.LENGTH_SHORT).show();
            }
        });





        btnConnect.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if (bt.getServiceState() == BluetoothState.STATE_CONNECTED) {
                    bt.disconnect();
                } else {
                    Intent intent = new Intent(getApplicationContext(), DeviceList.class);
                    startActivityForResult(intent, BluetoothState.REQUEST_CONNECT_DEVICE);
                }
            }
        });
    }



    public void onDestroy() {
        super.onDestroy();
        bt.stopService(); //블루투스 중지
    }

    public void onStart() {
        super.onStart();
        if (!bt.isBluetoothEnabled()) { //
            Intent intent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivityForResult(intent, BluetoothState.REQUEST_ENABLE_BT);
        } else {
            if (!bt.isServiceAvailable()) {
                bt.setupService();
                bt.startService(BluetoothState.DEVICE_OTHER); //DEVICE_ANDROID는 안드로이드 기기 끼리

            }
        }
    }



    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == BluetoothState.REQUEST_CONNECT_DEVICE) {
            if (resultCode == Activity.RESULT_OK)
                bt.connect(data);
        } else if (requestCode == BluetoothState.REQUEST_ENABLE_BT) {
            if (resultCode == Activity.RESULT_OK) {
                bt.setupService();
                bt.startService(BluetoothState.DEVICE_OTHER);

            } else {
                Toast.makeText(getApplicationContext()
                        , "Bluetooth was not enabled."
                        , Toast.LENGTH_SHORT).show();
                finish();
            }
        }
    }
}

