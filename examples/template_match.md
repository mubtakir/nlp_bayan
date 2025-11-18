# Templates & Match — القوالب والمطابقة

Domain: logic

```bayan
hybrid {
  النص = "سافر خالد إلى مكة"
  tpl = template("سافر {اسم} إلى {مدينة}")
  m = match(tpl, النص)
  if m {
    print(m["اسم"])
    print(m["مدينة"])
  }
  out = render(tpl, {"اسم":"سعد", "مدينة":"الرياض"})
  print(out)
}
```

