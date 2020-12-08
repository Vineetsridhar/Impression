import React from 'react'
import { TouchableOpacity, Image, ImageProps, Linking, Alert, View } from 'react-native'
interface props {
    position: number,
    link?: string
}
export default function LinkImage({ position, link }: props):JSX.Element {
    if (!link) return <View/>;

    let source: ImageProps;

    const openLink = () => {
        Linking.canOpenURL(link).then(canOpenURL => {
            if (canOpenURL) {
                Linking.openURL(link)
            } else {
                Alert.alert("Error", "Cannot open URL")
            }
        })
    }

    if (position == 0) {
        source = require('../assets/img/github.png')
    } else {
        source = require('../assets/img/linkedin.png')
    }
    return (
        <TouchableOpacity onPress={openLink}>
            <Image source={source} style={{ width: 100, height: 100, resizeMode: 'contain' }} />
        </TouchableOpacity>
    )
}