
# This script takes the table here:
# http://jenny.tfrec.wsu.edu/opm/CMDDLookupWObiofix.pdf
# after it's been edited to include the missing
# min and max degrees, and reshapes it from "wide"
# to "long" format, to simplify table lookup.

library(reshape2)

DegreeDayCM <- read.csv("D:/Projects/degreeday/data/DegreeDayCM.csv", stringsAsFactors=FALSE)

dd <- melt(DegreeDayCM,"MaxTemp")

# Renaming columns
names(dd)[names(dd)=="variable"] <- "MinTemp"
names(dd)[names(dd)=="value"] <- "DegreeDay"

# Rename min temp levels
for (level in levels(dd$MinTemp)) {
  newLevel <- gsub("X","",level)
  levels(dd$MinTemp)[levels(dd$MinTemp)==level] <- newLevel
}

write.csv(dd, "D:/Projects/degreeday/data/DegreeDayCM_Long.csv")
