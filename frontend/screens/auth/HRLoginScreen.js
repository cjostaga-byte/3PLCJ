import React from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const HRLoginScreen = () => {
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');

    const handleLogin = () => {
        // Handle login logic
        console.log('Logging in with', username, password);
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>HR Login</Text>
            <TextInput 
                style={styles.input} 
                placeholder="Username" 
                value={username} 
                onChangeText={setUsername} 
            />
            <TextInput 
                style={styles.input} 
                placeholder="Password" 
                secureTextEntry 
                value={password} 
                onChangeText={setPassword} 
            />
            <Button title="Login" onPress={handleLogin} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        padding: 20,
    },
    title: {
        fontSize: 24,
        marginBottom: 20,
        textAlign: 'center',
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 20,
        paddingLeft: 8,
    },
});

export default HRLoginScreen;