import React, { useState } from 'react';
import { View, Text, TextInput, Image, ScrollView, TouchableOpacity } from 'react-native';
import { Avatar } from 'react-native-elements';
import styles from './ProfileStyle';
import avatar from '../../config/avatar';
import FormItem from '../components/FormItem';

export default function ProfileScreen() {
	return (
		<ScrollView style={styles.container} contentContainerStyle={{alignItems:'center'}}>
			<TouchableOpacity onPress={()=>{}}>
				<Image style={styles.avatarStyle} source={{ uri: avatar }} />
			</TouchableOpacity>

			<Text style={styles.title}>Name</Text>
			<View style={styles.rowContainer}>
				<TextInput style={[styles.nameStyle, {marginRight:4}]} placeholder="First Name" />
				<TextInput style={[styles.nameStyle, {marginLeft: 4}]} placeholder="Last Name" />
			</View>

			<FormItem 
				title="School/Organization" 
				placeholder="NJIT"
			/>
			<FormItem 
				title="Email" 
				placeholder="email@email.com"
			/>

			<FormItem 
				title="About you" 
				placeholder="I am a..."
				style={{height:100}}
			/>
			<FormItem 
				title="GitHub" 
				placeholder="https://www.github.com"
			/>
			<FormItem 
				title="LinkedIn" 
				placeholder="https://www.linkedin.com"
				style={{height:100}}
			/>
			<TouchableOpacity onPress={()=> {}}>
				<Text style={styles.link}>Download Resume</Text>
			</TouchableOpacity>
		</ScrollView>
	)
}
