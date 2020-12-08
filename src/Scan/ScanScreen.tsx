import React, { useState, useEffect } from "react";
import {
  Text,
  StyleSheet,
  InteractionManager,
  ToastAndroid,
  View,
} from "react-native";
import { Camera } from "expo-camera";
import metrics from "../../config/metrics";
import FAB from "../components/FAB";
import { AntDesign } from "@expo/vector-icons";
import { newConnection } from "../helpers/network";

export default function ScanScreen({ navigation }: any):JSX.Element {
  const [hasPermission, setHasPermission] = useState(false);
  const [ratio, setRatio] = useState("");
  const [displayCamera, setDisplayCamera] = useState(true);

  let blurListener: () => void, focusListener: () => void;

  const makeListeners = () => {
    blurListener = navigation.addListener("blur", () => {
      setDisplayCamera(false);
    });
    focusListener = navigation.addListener("focus", () => {
      setDisplayCamera(true);
    });
  };

  useEffect(() => {
    makeListeners();
    (async () => {
      const { status } = await Camera.requestPermissionsAsync();
      setHasPermission(status === "granted");
    })();
    return () => {
      focusListener();
      blurListener();
    };
  }, []);

  let camera: Camera | null;
  const updateStateForCameraProps = () => {
    InteractionManager.runAfterInteractions(async () => {
      const ratios = await camera?.getSupportedRatiosAsync();
      getBestRatio(ratios);
    });
  };

  const getBestRatio = (ratios: string[] | undefined) => {
    if(!ratios) return []
    const wantedRatio = (metrics.HEIGHT_PIXELS + 200) / metrics.WIDTH_PIXELS; //Ideal Ratio of phone. Added 200 to account for appBar
    let diff = 100;
    let curr = "";
    for (let i = 0; i < ratios.length; i++) {
      const nums = ratios[i].split(":");
      const h = parseInt(nums[0]);
      const w = parseInt(nums[1]);
      const val = Math.abs(h / w - wantedRatio); //Get the absolute difference between current ratio and wated ratio
      if (val < diff) {
        //Set variables equal to the lowest difference in ratios
        curr = ratios[i];
        diff = val;
      }
    }
    setRatio(curr);
  };

  const handleBarCodeScanned = ({
    type,
    data,
  }: {
    type: string;
    data: string;
  }) => {
    if (data.startsWith("impression://")) {
      const email = data.substr(13);
      newConnection(email)
        .then((response) => response.json())
        .then((json) => {
          if (json.hasOwnProperty("success") && !json["success"]) {
            ToastAndroid.show("There was an error with this QR code", ToastAndroid.LONG);
          } else
            navigation.navigate("Contacts", {
              screen: "ContactDetail",
              params: { user: json },
            });
        });
    }
  };

  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  if (!displayCamera) return <View/>;

  return (
    <Camera
      ref={(ref) => (camera = ref)}
      ratio={ratio}
      onBarCodeScanned={handleBarCodeScanned}
      style={StyleSheet.absoluteFillObject}
      onCameraReady={updateStateForCameraProps}
    >
      <FAB
        onPress={() => {
          navigation.push("QRCode");
        }}
      >
        <AntDesign name="qrcode" style={{ color: 'white', fontSize: 45 }} />
      </FAB>
    </Camera>
  );
}
