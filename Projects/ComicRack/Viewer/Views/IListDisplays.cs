﻿// Decompiled with JetBrains decompiler
// Type: cYo.Projects.ComicRack.Viewer.Views.IListDisplays
// Assembly: ComicRack, Version=1.0.5915.38777, Culture=neutral, PublicKeyToken=b3ca110c99b4b731
// MVID: E9032406-66BB-46BB-A802-D697DB44DA19
// Assembly location: C:\Program Files\ComicRack\ComicRack.exe

using cYo.Projects.ComicRack.Engine;
using System.Drawing;

namespace cYo.Projects.ComicRack.Viewer.Views
{
  public interface IListDisplays
  {
    void AddListWindow(Image tabImage, IComicBookListProvider bookList);

    void AddListTab(Image tabImage, IComicBookListProvider bookList);

    void RemoveList(IComicBookListProvider bookList, object hint);
  }
}
