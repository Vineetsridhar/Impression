import React from 'react'
import { StyleSheet, TouchableOpacity } from 'react-native'
import colors from '../../config/colors'

interface props {
    onPress: ()=>void;
    children: JSX.Element
}
export default function FAB({onPress, children}:props){
    return (
        <TouchableOpacity style={styles.floatingActionButton} onPress={onPress}>
            {children}
        </TouchableOpacity>
    )
}

const styles = StyleSheet.create({
    floatingActionButton:{
        position:'absolute',
        display:'flex',
        justifyContent:'center',
        alignItems:'center',
        bottom: 16,
        right: 16,
        height: 60,
        width: 60,
        borderRadius: 30,
        backgroundColor:colors.main,
        elevation: 5,
        zIndex: 5
    }
})