import React from 'react';
import { View, Text, TextInput } from 'react-native';
import { Avatar } from 'react-native-elements';
import styles from './ProfileStyle';

export default function ProfileScreen(){
    return (
        <View style={ styles.container }>
		<Avatar    
			size="xlarge"
			rounded
	    		icon={{ name: 'user', type: 'font-awesome' }}
			onPress={() => console.log("Works!")}
		    	activeOpacity={0}
	 	/>
		<Text>FirstName LastName</Text>
		<View style={ styles.rowContainer }>
			<View style={ styles.flexCode }>
				<TextInput 
				multiline
				style={ styles.schoolStyle } 
				placeholder="Harvard University"
				/>
			</View>
		
			<View style={ styles.flexCode }>
				<TextInput 
				multiline
				style={ styles.emailStyle } 
				placeholder="email@email.com"
				/>
			</View>
		</View>
		<View style={ styles.container }>
			<TextInput style={ styles.linksStyle } placeholder="https://www.github.com"/>
			<TextInput style={ styles.linksStyle } placeholder="https://www.linkedin.com"/>
			<TextInput style={ styles.linksStyle } placeholder="Download Resume"/>
		</View>	
        </View> 
    )
}
