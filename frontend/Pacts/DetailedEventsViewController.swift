//
//  DetailedEventsViewController.swift
//  Pacts
//
//  Created by Angela Chen on 8/28/20.
//  Copyright © 2020 Angela Chen. All rights reserved.
//

import UIKit
import FSCalendar

class DetailedEventsViewController: UIViewController, FSCalendarDelegate {
    
    @IBOutlet var calendar: FSCalendar!
    
    //var datesWithEvent = ["25-08-2020"]
    override func viewDidLoad() {
        super.viewDidLoad()
        calendar.delegate = self
        // Do any additional setup after loading the view.
    }
    
    func calendar(_ calendar: FSCalendar, didSelect date: Date, at monthPosition: FSCalendarMonthPosition) {
            let formatter = DateFormatter()
        formatter.dateFormat = "EEEE MM-dd-YYYY"
        let string = formatter.string(from: date)
        print("\(string)")
    }
//
//    func calendar(_ calendar: FSCalendar, numberOfEventsFor date: Date) -> Int {
//        let formatter = DateFormatter()
//        formatter.dateFormat = "dd-MM-yyyy"
////        guard let eventDate = formatter.date(from: "22-08-2020") else {
////            return 0}
////        if date.compare(eventDate) == .orderedSame {
////            return 2
////        }
//
//         return 0
//    }
    var datesWithEvent = ["2020-08-03", "2020-08-06", "2020-08-12", "2020-08-25"]

    var datesWithMultipleEvents = ["2020-08-09", "2020-08-17", "2015-10-20", "2015-08-28"]

    fileprivate lazy var dateFormatter2: DateFormatter = {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd"
        return formatter
    }()

    func calendar(_ calendar: FSCalendar, numberOfEventsFor date: Date) -> Int {

        let dateString = self.dateFormatter2.string(from: date)

        if self.datesWithEvent.contains(dateString) {
            return 1
        }

        if self.datesWithMultipleEvents.contains(dateString) {
            return 3
        }

        return 0
    }
    

   }



