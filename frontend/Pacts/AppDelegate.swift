//
//  AppDelegate.swift
//  Pacts
//
//  Created by Angela Chen on 8/27/20.
//  Copyright © 2020 Angela Chen. All rights reserved.
//

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        
        window = UIWindow(frame: UIScreen.main.bounds)
        window?.rootViewController = UINavigationController(rootViewController: UITabBarController())
        window?.makeKeyAndVisible()
        
        //color of the tab bar
        UITabBar.appearance().barTintColor = UIColor(red: 255/255, green: 255/255, blue: 255/255, alpha: 1.0)
        //color of the selection color
        UITabBar.appearance().tintColor = UIColor(red: 63/255, green: 63/255, blue: 63/255, alpha: 0.7)
        UITabBar.appearance().isTranslucent = false
        return true
    }

    // MARK: UISceneSession Lifecycle

    func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        // Called when a new scene session is being created.
        // Use this method to select a configuration to create the new scene with.
        return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
    }

    func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
        // Called when the user discards a scene session.
        // If any sessions were discarded while the application was not running, this will be called shortly after application:didFinishLaunchingWithOptions.
        // Use this method to release any resources that were specific to the discarded scenes, as they will not return.
    }


}

